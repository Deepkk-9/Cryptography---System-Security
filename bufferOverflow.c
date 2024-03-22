#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int auth = 0;
    char sysPassword[16] = "secret";
    char userPassword[16];

    printf("Enter your password : ");
    scanf("%s", userPassword);

    if (strcmp(userPassword, sysPassword) == 0)
    {
        auth = 1;
    }

    printf("User Password: %s\n", userPassword);
    printf("System Password: %s\n", sysPassword);
    printf("Address at User Password: %p\n", userPassword);
    printf("Address at System Password: %p\n", sysPassword);
    printf("Address at Auth: %p\n", &auth);
    printf("Auth Variable: %p\n", auth);

    if (auth)
    {
        printf("Password is correct!\n");
    }
    else
    {
        printf("Password Incorrect!\n");
    }

    return 0;
}