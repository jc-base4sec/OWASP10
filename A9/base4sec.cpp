#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void welcome(){
	printf("\n--------------");
	printf("\n BIENVENIDOS\n      A\n-=[BASE4Sec]=-\n");
	printf("--------------\n");
}

void buggets(){
	char pais [500];
	memset(pais, '\0', sizeof(pais));
	
	printf("\nPais     (menor a 500 caracteres): ");
	gets(pais);
	printf(" -> Pais registrado %s", pais);
}

void bugsprintf(){
	char *ciudad;
	char dest [200];
	ciudad=(char*)malloc(500);
	memset(dest, '\0', sizeof(ciudad));
	
	printf("\n\nCiudad   (menor a 200 caracteres): ");
	scanf("%s", ciudad);
	sprintf(dest, "%s", ciudad);
	printf(" -> Ciudad registrado %s", dest);
}

void bugscanf(){
	char nombre [500];
	memset(nombre, '\0', sizeof(nombre));
	
	printf("\n\nNombre   (menor a 500 caracteres): ");	
	scanf("%s", nombre);
	printf(" -> Nombre registrado %s", nombre);
}

void bugstrcpy(){
	char *apellido;
	char dest [500];
	apellido=(char*)malloc(1000);
	memset(apellido, '\0', sizeof(apellido));
	memset(dest, '\0', sizeof(dest));
	
	printf("\n\nApellido (menor a 500 caracteres): ");
	scanf("%s", apellido);
	strcpy(dest, apellido);
	printf(" -> Apellido registrado %s", dest);
}

void buguaf(){
	int n;
	char *buffer;
	buffer = (char*)malloc(101);
	memset(buffer, '\0', sizeof(buffer));
	
	for (n=0; n<100; n++){
		buffer[n]='A';
	}
	buffer[100]='\0';
	
	printf ("\n\nLlave del usuarios:");
	printf ("\n -> Cadena aleatoria: %s", buffer);
  	free(buffer);
}

void bugformat(){
	int i,n;
	char * format;
	char password[13]="AAA_secretB4";
	
	printf ("\n\nElige un size para tu buffer: ");
	scanf ("%d", &i);
	format = (char*)malloc(i+1);
	memset(format, '\0', sizeof(format));
	
	printf("Ingrese valores para almacenar en el buffer: ");
	scanf("%s", format);
	
	printf(" -> Contenido del buffer: ");
	printf(format);
}

int main(int argc, char** argv){
    
	welcome();
	buggets();
	bugsprintf();
	bugscanf();
	bugstrcpy();
	buguaf();
	bugformat();
	
	return 0;
}
