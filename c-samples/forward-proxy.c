#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <netdb.h>
#include <sys/socket.h>
#include <arpa/inet.h>

char *get_peer_ip(char *hostname) {
        char *tmp = malloc(20);

        struct hostent *he;
        struct in_addr **addr_list;
        printf("Called for host %s\n", hostname);
        he = gethostbyname(hostname);
        if(he < 0) {
                perror("gethost");
        }
        addr_list = (struct in_addr **)he->h_addr_list;

        inet_ntop(AF_INET, (void *)addr_list[0], tmp, INET_ADDRSTRLEN);

        return tmp;
}

int connect_to_host(char* host, char* request, char* server_message){
    int socket_desc;
    struct sockaddr_in server_addr;
    char client_message[2000];
    printf("REQUEST: %s", request);

    // Clean buffers:
    memset(server_message,'\0',sizeof(server_message));
    memset(client_message,'\0',sizeof(client_message));

    // Create socket:
    socket_desc = socket(AF_INET, SOCK_STREAM, 0);

    if(socket_desc < 0){
        printf("Unable to create socket\n");
        return -1;
    }

    printf("Socket created successfully\n");
    char* host_ip = get_peer_ip(host);

    // Set port and IP the same as server-side:
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(80);
    server_addr.sin_addr.s_addr = inet_addr(host_ip);

    printf("%s ip is %s\n",host, host_ip);

    // Send connection request to server:
    if(connect(socket_desc, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0){
        printf("Unable to connect\n");
        return -1;
    }
    printf("Connected with server successfully\n");

    // Send the message to server:
    if(send(socket_desc, request, strlen(request), 0) < 0){
        printf("Unable to send message\n");
        return -1;
    }

    // Receive the server's response:
    if(recv(socket_desc, server_message, 2000, 0) < 0){
        printf("Error while receiving server's msg\n");
        return -1;
    }

    printf("Server's response: %s\n",server_message);

    // Close the socket:
    close(socket_desc);

    return 0;
}

int main(void)
{
    int socket_desc, client_sock, client_size;
    struct sockaddr_in server_addr, client_addr;
    char server_message[2000], client_message[2000], request[2000];

    // Clean buffers:
    memset(server_message, '\0', sizeof(server_message));
    memset(client_message, '\0', sizeof(client_message));

    // Create socket:
    socket_desc = socket(AF_INET, SOCK_STREAM, 0);

    if(socket_desc < 0){
        printf("Error while creating socket\n");
        return -1;
    }
    printf("Socket created successfully\n");

    // Set port and IP:
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(2000);
    server_addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    // Bind to the set port and IP:
    if(bind(socket_desc, (struct sockaddr*)&server_addr, sizeof(server_addr))<0){
        printf("Couldn't bind to the port\n");
        return -1;
    }
    printf("Done with binding\n");

    // Listen for clients:
    if(listen(socket_desc, 1) < 0){
        printf("Error while listening\n");
        return -1;
    }
    printf("\nListening for incoming connections.....\n");

    // Accept an incoming connection:
    client_size = sizeof(client_addr);
    client_sock = accept(socket_desc, (struct sockaddr*)&client_addr, &client_size);

    if (client_sock < 0){
        printf("Can't accept\n");
        return -1;
    }
    printf("Client connected at IP: %s and port: %i\n", inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port));

    // Receive client's message:
    if (recv(client_sock, client_message, sizeof(client_message), 0) < 0){
        printf("Couldn't receive\n");
        return -1;
    }
    printf("Msg from client: %s\n", client_message);

    char *saveptr1, *saveptr2, *str1, *str2, *token, *subtoken, *host;
    str1 = client_message;
    strcpy(request, client_message);
    for (int j = 1; ; j++, str1 = NULL) {
        token = strtok_r(str1, "\r\n", &saveptr1);
        if (token == NULL)
                break;
        printf("%d: %s\n", j, token);
        int i = 1;
        for (str2 = token; ;str2 = NULL ) {
                subtoken = strtok_r(str2, " ", &saveptr2);
                if (subtoken == NULL)
                        break;
                if (i == 2 && j == 2)
                        host = subtoken;
                printf("%s\n", subtoken);
                i++;
        }
    }

    printf("Host: %s\n", host);
    if (server_message,connect_to_host(host,request,server_message) != 0)
            return -1;

    // Respond to client:
    //strcpy(server_message, "This is the server's message.");

    if (send(client_sock, server_message, strlen(server_message), 0) < 0){
        printf("Can't send\n");
        return -1;
    }

    // Closing the socket:
    close(client_sock);
    close(socket_desc);

    return 0;
}
