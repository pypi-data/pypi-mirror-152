#include "write_dpbin.h"
// from libediom project /tools/covertdat.c on pymodule_sz branch
const char binfn[128]="test.bin";
const char datfn[128]="test.dat";
// FILE *binf;

typedef struct GPAR2 {
    short int indx[3];
    short int id; /* 0 not defined, 1 x and y defined, 2 all defined*/
    double par[5]; /* length, x, y, int*/
} GPAR2;

typedef struct DPPARHead {	
    short int j,m;
    int ng;
    double u,v, bm[3];
} DPPARHead;

typedef struct DPPAR {
    DPPARHead dp_head;
    GPAR2 *gl; 
} DPPAR;

typedef struct DPHeader {
	double theta, dx, uvw[4][3], xy[4][2], ad[3][3], gmx[3][3], gmr[3][3];
	int np, ndp;
} DPHeader;

DPHeader dpp;

int StrComp(char *s1, char *s2, int n) 
{
   int k;
   k = strlen(s1);
   if (n>k) n=k;
   for (k=0; k<n; ++k) 
     if (s1[k] != s2[k]) return 0;
   return 1;
}
void deleteDP(DPPAR *dpp, const int ndp){
	int j;
	if (dpp) {
		for(j=0;j<ndp;j++){
			if(dpp[j].gl) free(dpp[j].gl);
		}
		free(dpp);
	}
}
// void printWRError(const char* fn)
// {
// 	printf("Error: reading input binary file: %s\n", ifn);
// 	perror("Error:");
// }

void printDPHead(const int ith, const DPPARHead *h){
	printf("#\nDP   %d\n %hd %hd %f %f %f %f %f\n", ith+1,
			h->j, h->m,
			h->u, h->v,
			h->bm[0], h->bm[1], h->bm[2]);
	return;
}
void printDPLine(const int ith, const GPAR2 *dpline){
	printf("%hd %hd %hd %f %f %f %f %f\n", 
		dpline->indx[0], dpline->indx[1], dpline->indx[2],
		dpline->par[0], dpline->par[1], dpline->par[2], dpline->par[3], dpline->par[4]);
}
// int dp_convert_binary(const char* fn, const char* ext, const char* destdir)
int dpwritebin(void)
{
    FILE *infile, *outfile;  
	char string[129];
	// char ifn[129]="";
	// char destPath[256];
    DPHeader* dpl = &dpp;
	DPPAR *dp = NULL;
	GPAR2 *gp = NULL;
    int i, j, nsp, np, ng,werr;
	long dplist_size, dp_bsize;
	// int err;
	size_t ret = 0;
/*
       input file is text format
       output file is binary format
*/
	
	infile = fopen(datfn, "r");
	if ( !infile ) {
		printf("Error opening input file for read: %s\n",  datfn );
		return 1;
	}

	if (fgets(string, 128, infile) == NULL) return 2;
	if (!StrComp(string, "#!dmap", 6)) {
		printf("Error reading input file 2: %s\n", datfn);
		return 2;
	}
	while (1) {
		if (fgets(string, 128, infile) == NULL) {			
			printf("Error reading input file 3: %s\n", datfn);
			return 3;
		}
		if (StrComp(string, "np", 2)) break;
	}
       sscanf(string + 2, "%d", &np);
       if (np > 4) np = 4; //maximum 4
	dpl->np = np;
	for (i = 0; i < np; i++) {
		if (fgets(string, 128, infile) == NULL) return 6;
		sscanf(string, "%lf %lf %lf %lf %lf",
			&dpl->uvw[i][0], &dpl->uvw[i][1],
			&dpl->uvw[i][2], &dpl->xy[i][0],
			&dpl->xy[i][1]);
	}
	while (1) {
		if (fgets(string, 128, infile) == NULL) {			
			printf("Error reading input file 3: %s\n", datfn);
			return 3;
		}
		if (StrComp(string, "AD", 2)) {
			for (i = 0; i < 3; i++) {
				if (fgets(string, 128, infile) == NULL) {			
					printf("Error reading input file 6: %s\n", datfn);
					return 6;
				}	
				sscanf(string, "%lf %lf %lf",&dpl->ad[0][i], &dpl->ad[1][i],&dpl->ad[2][i]);
			}
		} else if (StrComp(string, "GMX", 3)) {
			for (i = 0; i < 3; i++) {
				if (fgets(string, 128, infile) == NULL) {			
					printf("Error reading input file 6: %s\n", datfn);
					return 6;
				}	
				// printf("reading gmx: %s", string);
				sscanf(string, "%lf %lf %lf", &dpl->gmx[0][i], &dpl->gmx[1][i], &dpl->gmx[2][i]);
			}
		}
		else if (StrComp(string, "GMR", 3)) {
			for (i = 0; i < 3; i++) {
				if (fgets(string, 128, infile) == NULL) {			
					printf("Error reading input file 6: %s\n", datfn);
					return 7;
				}
				// printf("reading gmr: %s", string);	
				sscanf(string, "%lf %lf %lf", &dpl->gmr[0][i], &dpl->gmr[1][i], &dpl->gmr[2][i]);
			}
		}
		else if (StrComp(string, "dx", 2)){
			sscanf(string+2, "%lf", &dpl->dx);
		}
		else if (StrComp(string, "nsp", 3)) break;
	}

	sscanf(string + 3, "%d", &nsp);
	dpl->ndp = nsp;
	if (fgets(string, 128, infile) == NULL) {			
		printf("Error reading input file 4: %s\n", datfn);
		return 4;
	}	

	dplist_size = (long) nsp*sizeof(DPPAR);
	dp = (DPPAR *) malloc(dplist_size);
	if(dp==NULL){
		printf("Error allocating memory for dp list: %s\n", datfn);
		return 12;
	}

	for (i = 0; i<nsp; i++) {
		while (1) {
			if (fgets(string, 128, infile) == NULL) {			
				printf("Error reading input file 5: %s\n", datfn);
				return 5;
			}	
			if (StrComp(string, "DP", 2)) break;
		}
		if (fgets(string, 128, infile) == NULL) {			
			printf("Error reading input file 5: %s\n", datfn);
			return 5;
		}	
		// printf("DP head: %s", string);
		sscanf(string, "%hd %hd %lf %lf %lf %lf %lf",
			&(dp[i].dp_head.j), &(dp[i].dp_head.m),
			&(dp[i].dp_head.u), &(dp[i].dp_head.v),
			&(dp[i].dp_head.bm[0]), &(dp[i].dp_head.bm[1]), 
			&(dp[i].dp_head.bm[2]));
			
		if (fgets(string, 128, infile) == NULL) {			
			printf("Error reading input file 7: %s\n", datfn);
			return 7;
		}	
		sscanf(string, "%d", &ng);
		dp[i].dp_head.ng = ng;
		dp_bsize = ng*sizeof(GPAR2);
		gp = (GPAR2 *) malloc(dp_bsize);
		if(gp==NULL){
			printf("Error allocating memory for dp body at index=%d: %s\n", i, datfn);
			deleteDP(dp,nsp);
			return 12;
		}
		dp[i].gl=gp;
		
		for (j = 0; j<ng; j++) {
			if (fgets(string, 128, infile) == NULL) {			
				printf("Error reading input file 8: %s\n", datfn);
				deleteDP(dp,nsp);
				return 8;
			}	
			ret = sscanf(string, "%hd %hd %hd %lf %lf %lf %lf %lf",
				&(gp[j].indx[0]), &(gp[j].indx[1]), &(gp[j].indx[2]),
				&(gp[j].par[0]), &(gp[j].par[1]), &(gp[j].par[2]), 
				&(gp[j].par[3]), &(gp[j].par[4]));
			if(ret == EOF || ret != 8){			
				printf("Error reading DP body 10: %s\n", datfn);
				deleteDP(dp,nsp);
				return 10;
			}
			gp[j].par[2] *= -1; //check
			gp[j].id = 0;
		}
		gp=NULL;
	}
	
	fclose(infile);

	// overwrite if file exists

	outfile = fopen(binfn, "wb");
	if ( !outfile ) {
		printf("Error writing output file: %s\n", binfn);
		deleteDP(dp,nsp);
		return 4;
	}
	// printf("dx: %lf", dpl->dx);

	fwrite((DPHeader* )dpl, sizeof(DPHeader),1,outfile);
	if(dp == NULL){
		return 12;
	}
	for (i = 0; i<nsp; i++) {
		fwrite((DPPARHead *)&(dp[i].dp_head), sizeof(DPPARHead), 1, outfile);
		
		// printf("in convert: done with file writing for dp head\n");
		for(j = 0; j < dp[i].dp_head.ng; j++){
			fwrite((GPAR2 *)&(dp[i].gl[j]), sizeof(GPAR2), 1, outfile);
		}
		// printf("in convert: done with file writing for dp body\n");
	}
	// printf("in convert: done with file writing for dp before\n");
	// clean up!
    fclose(outfile);
	deleteDP(dp,nsp);
	
	// printf("in convert: done with file writing for dp\n");
    return 0;
}
int dpwritebin_new(const char *datfn1, const char *datext)
{
    FILE *infile, *outfile;  
	char string[256];
	char ifn[129]="";
	char ofn[129]="";
	// char destPath[256];
    DPHeader* dpl = &dpp;
	DPPAR *dp = NULL;
	GPAR2 *gp = NULL;
    int i, j, nsp, np, ng,werr;
	size_t dplist_size, dp_bsize;
	// int err;
	size_t ret = 0;
/*
       input file is text format
       output file is binary format
*/	
	strcpy(ifn, datfn1);
	strcat(ifn, ".");
	strcat(ifn, datext);

	
	// strcpy(ofn, "Diamond_small.bin");

	strcpy(ofn, datfn1);
	strcat(ofn, ".bin");
	// printf("Binary otuput file name: %s\n", ofn);

	infile = fopen(ifn, "r");
	if ( !infile ) {
		printf("Error opening input file for read: %s\n", ifn);
		return 1;
	}

	if (fgets(string, 128, infile) == NULL) return 2;
	if (!StrComp(string, "#!dmap", 6)) {
		printf("Error reading input file 2: %s\n", ifn);
		return 2;
	}
	while (1) {
		if (fgets(string, 128, infile) == NULL) {			
			printf("Error reading input file 3: %s\n", ifn);
			return 3;
		}
		if (StrComp(string, "np", 2)) break;
	}
       sscanf(string + 2, "%d", &np);
       if (np > 4) np = 4; //maximum 4
	dpl->np = np;
	for (i = 0; i < np; i++) {
		if (fgets(string, 128, infile) == NULL) return 6;
		sscanf(string, "%lf %lf %lf %lf %lf",
			&dpl->uvw[i][0], &dpl->uvw[i][1],
			&dpl->uvw[i][2], &dpl->xy[i][0],
			&dpl->xy[i][1]);
	}
	while (1) {
		if (fgets(string, 128, infile) == NULL) {			
			printf("Error reading input file 3: %s\n", ifn);
			return 3;
		}
		if (StrComp(string, "AD", 2)) {
			for (i = 0; i < 3; i++) {
				if (fgets(string, 128, infile) == NULL) {			
					printf("Error reading input file 6: %s\n", ifn);
					return 6;
				}	
				sscanf(string, "%lf %lf %lf",&dpl->ad[0][i], &dpl->ad[1][i],&dpl->ad[2][i]);
			}
		} else if (StrComp(string, "GMX", 3)) {
			for (i = 0; i < 3; i++) {
				if (fgets(string, 128, infile) == NULL) {			
					printf("Error reading input file 6: %s\n", ifn);
					return 6;
				}	
				// printf("reading gmx: %s", string);
				sscanf(string, "%lf %lf %lf", &dpl->gmx[0][i], &dpl->gmx[1][i], &dpl->gmx[2][i]);
			}
		}
		else if (StrComp(string, "GMR", 3)) {
			for (i = 0; i < 3; i++) {
				if (fgets(string, 128, infile) == NULL) {			
					printf("Error reading input file 6: %s\n", ifn);
					return 7;
				}
				// printf("reading gmr: %s", string);	
				sscanf(string, "%lf %lf %lf", &dpl->gmr[0][i], &dpl->gmr[1][i], &dpl->gmr[2][i]);
			}
		}
		else if (StrComp(string, "dx", 2)){
			sscanf(string+2, "%lf", &dpl->dx);
		}
		else if (StrComp(string, "nsp", 3)) break;
	}

	sscanf(string + 3, "%d", &nsp);
	dpl->ndp = nsp;
	if (fgets(string, 128, infile) == NULL) {			
		printf("Error reading input file 4: %s\n", ifn);
		return 4;
	}	

	dplist_size = (size_t) (nsp*sizeof(DPPAR));
	dp = (DPPAR *) malloc(dplist_size);
	if(dp==NULL){
		printf("Error allocating memory for dp list: %s\n", ifn);
		return 12;
	}

	for (i = 0; i<nsp; i++) {
		while (1) {
			if (fgets(string, 128, infile) == NULL) {			
				printf("Error reading input file 5: %s\n", ifn);
				return 5;
			}	
			if (StrComp(string, "DP", 2)) break;
		}
		if (fgets(string, 128, infile) == NULL) {			
			printf("Error reading input file 5: %s\n", ifn);
			return 5;
		}	
		// printf("DP head: %s", string);
		sscanf(string, "%hd %hd %lf %lf %lf %lf %lf",
			&(dp[i].dp_head.j), &(dp[i].dp_head.m),
			&(dp[i].dp_head.u), &(dp[i].dp_head.v),
			&(dp[i].dp_head.bm[0]), &(dp[i].dp_head.bm[1]), 
			&(dp[i].dp_head.bm[2]));
			
		if (fgets(string, 128, infile) == NULL) {			
			printf("Error reading input file 7: %s\n", ifn);
			return 7;
		}	
		sscanf(string, "%d", &ng);
		dp[i].dp_head.ng = ng;
		dp_bsize = (size_t)(ng*sizeof(GPAR2));
		gp = (GPAR2 *) malloc(dp_bsize);
		if(gp==NULL){
			printf("Error allocating memory for dp body at index=%d: %s\n", i, ifn);
			deleteDP(dp,nsp);
			return 12;
		}
		dp[i].gl=gp;
		
		for (j = 0; j<ng; j++) {
			if (fgets(string, 128, infile) == NULL) {			
				printf("Error reading input file 8: %s\n", ifn);
				deleteDP(dp,nsp);
				return 8;
			}	
			ret = sscanf(string, "%hd %hd %hd %lf %lf %lf %lf %lf",
				&(gp[j].indx[0]), &(gp[j].indx[1]), &(gp[j].indx[2]),
				&(gp[j].par[0]), &(gp[j].par[1]), &(gp[j].par[2]), 
				&(gp[j].par[3]), &(gp[j].par[4]));
			if(ret == EOF || ret != 8){			
				printf("Error reading DP body 10: %s\n", ifn);
				deleteDP(dp,nsp);
				return 10;
			}
			gp[j].par[2] *= -1; //check
			gp[j].id = 0;
		}
		// gp=NULL;
	}
	
	fclose(infile);

	// overwrite if file exists

	outfile = fopen(ofn, "wb");
	if ( !outfile ) {
		printf("Error writing output file: %s\n", ofn);
		deleteDP(dp,nsp);
		return 4;
	}

	if (fwrite(dpl, sizeof(DPHeader),1,outfile) != 1){
		perror("error");
		return 18;
	}

	for (i = 0; i<nsp; i++) {
		if(fwrite(&(dp[i].dp_head), sizeof(DPPARHead), 1, outfile) !=1)
		{
			perror("Error writing dphead: ");
			return 17;
		}
		for(j = 0; j < dp[i].dp_head.ng; j++){
			if( fwrite(&(dp[i].gl[j]), sizeof(GPAR2), 1, outfile) != 1)
			{
				perror("Error");
				return 15;
			}
		}
	}
	// clean up!
	deleteDP(dp,nsp);
    if(outfile != NULL){
		if( fclose(outfile) != 0 ) {
			perror("Error: closing binary file!");
			return 13;
		}
	} else{
		return 14;
	}

	if( remove(ifn) != 0){
		printf("Warning: .dat file %s removal failed", ifn);
		return 16;
	}
	
	// printf("in convert: done with file writing for dp\n");
    return 0;
}
void print_header(const DPHeader *dp){
	int np,i;
	// char string[129];

	np = dp->np;
	printf("np %d\n",np);
	for (i = 0; i < np; i++) {
		printf("%lf %lf %lf %lf %lf\n",
			dp->uvw[i][0], dp->uvw[i][1],
			dp->uvw[i][2], dp->xy[i][0],
			dp->xy[i][1]);
	}
	
	printf("AD\n");

	for (i = 0; i < 3; i++) {
		printf("%lf %lf %lf\n",dp->ad[0][i], dp->ad[1][i],dp->ad[2][i]);
	}

	printf("GMX\n");

	for (i = 0; i < 3; i++) {
		printf("%lf %lf %lf\n",dp->gmx[0][i], dp->gmx[1][i],dp->gmx[2][i]);
	}

	printf("GMR\n");

	for (i = 0; i < 3; i++) {
		printf("%lf %lf %lf\n",dp->gmr[0][i], dp->gmr[1][i],dp->gmr[2][i]);
	}

	printf("dx %lf\n", dp->dx);
	printf("nsp %d\n", dp->ndp);
	return;
}


int dpreadbinary(const char *binfn1, const char *binext)
{
	FILE *infile;
	char ifn[128]="";
	DPHeader dph;
	// int err;
	// char destPath[256];
	DPPARHead dprh;
	GPAR2 dpline;
	DPPAR *dp;
	int i, j;
	size_t ret;

/*
       input file is text format
       output file is binary format
// */	
	strcpy(ifn, binfn1);
	strcat(ifn, ".");
	strcat(ifn, binext);
	
	infile = fopen(ifn, "rb");
	
	if ( infile == NULL ) {
		printf("Error opening input binary file: %s\n", ifn);
		perror("Error reading input binary file");
		return -1;
	}

	ret = fread(&dph, sizeof(DPHeader), 1, infile);
	if (ret != 1) {
		perror("Error reading binary file");
		return -5;
	}
	print_header(&dph);
    if (infile == NULL){
		printf("Error closing input binary file: %s\n", ifn);
        return -2;
    }
	
	for (i=0; i < dph.ndp; i++){
		ret = fread(&dprh, sizeof(DPPARHead), 1, infile);
		printDPHead(i,(DPPARHead *)&dprh);
		if (ret != 1) {
			perror("Error reading dphead");
			return -3;
		}

		for(int j = 0; j < dprh.ng; j++){
			ret = fread(&dpline, sizeof(GPAR2), 1, infile);
			if (ret != 1) {
				perror("Error");
				return -4;
			}
			printDPLine(j, (GPAR2 *)&dpline);
		}
	}
    if( !infile) 
		return -6;
	fclose(infile);
	return 0;
}

// void setdpheaderuvw(double uvw[4][3])
// {
//     for ( int i = 0; i < 4; ++i ){
//         for( int j = 0; j < 3; ++j)
//         {
//             dpp.uvw[i][j] = uvw[i][j];
//         }
//     }
// }
// //     // dpp.uvw = uvw;
// // }
// void setdpheaderxy(double xy[4][2])
// {
//     for ( int i = 0; i < 4; ++i )
//         for( int j = 0; j < 2; ++j)
//         {
//             dpp.xy[i][j] = xy[i][j];
//         }
// }

// void setdpheadergmxr(double gmx[3][3], double gmr[3][3])
// {
//     for ( int i = 0; i < 3; ++i )
//         for( int j = 0; j < 3; ++j)
//         {
//             dpp.gmx[i][j] = gmx[i][j];
//             dpp.gmr[i][j] = gmr[i][j];
//         }
// }

// int openwritedpbin(void)
// {
//     int ret = 0;
//     printf("got to c program: %s\n", binfn);
//     binf = fopen(binfn, "wb");
//     printf("open in c program\n");
//     if (binf == NULL)
//     {
//         printf("Error: writing to dp data file!");
//         ret = 1;
//     }
//     return ret;
// }

// int closewritedpbin(void)
// {
//     printf("got to c program: close");
//     if (binf == NULL)
//     {
//         printf("Error: closing to dp data file!");
//         return 1;
//     }
//     close(binf);
//     return 0;
// }

// void setdpheadernums(int *np, int *ndp, double *d)
// {  
//     FILE *binf = NULL;
// 	int err;
//     size_t ret = 0;
//     // int arr[3] ={10,20,30};
//     printf("in c before fwrite %d\n", *np);
//     dpp.dx = *d;
//     dpp.np = *np;
//     dpp.ndp = *ndp;
//     // dpp.xy = xy;
//     // dpp.gmx = gmx;
//     // dpp.gmr = gmr;
//     err = fopen_s(&binf, binfn, "wb");
//     if( err != 0 ){
//         printf("Error: writing dp header data\n");
//         return;
//     }
//     printf("in c before fwrite\n");
//     ret = fwrite(&dpp, sizeof(DPHeader), 1, binf);
//     if( ret != 1){
//         printf("error writing int!");
//         return;
//     }
//     printf("in c after fwrite\n");
//     // if( binf == NULL){
//     //     printf("Error: closing dp header data\n");
//     //     return;
//     // }
//     printf("in c program %d,%d,%lf\n", dpp.np,dpp.ndp,dpp.dx);
//     err = fclose(binf);
// 	if (err != 0) {
// 		printf("Error: closing file");
// 	}
//     printf("in c after fclose\n");
// }