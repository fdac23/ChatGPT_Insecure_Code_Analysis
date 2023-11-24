#include <stdio.h>
#include <string.h>
#include <microhttpd.h>

int http_hello_page(void *cls, struct MHD_Connection *connection, const char *url, const char *method, const char *version, const char *upload_data, size_t *upload_data_size, void **con_cls) {
    const char *page = "<html><body><h1>Hello, %s!</h1></body></html>";
    const char *username = MHD_lookup_connection_value(connection, MHD_GET_ARGUMENT_KIND, "username");
    struct MHD_Response *response;
    int ret;

    if (strcmp(url, "/hello") == 0) {
        if (*con_cls == NULL) {
            *con_cls = (void *)1;
            return MHD_YES;
        } else if (*con_cls == (void *)1) {
            *con_cls = NULL;

            char response_buffer[256];
            snprintf(response_buffer, sizeof(response_buffer), page, username ? username : "World");

            response = MHD_create_response_from_buffer(strlen(response_buffer), (void *)response_buffer, MHD_RESPMEM_PERSISTENT);
            ret = MHD_queue_response(connection, MHD_HTTP_OK, response);
            MHD_destroy_response(response);
            return ret;
        }
    }

    return MHD_NO;
}

int main() {
    struct MHD_Daemon *daemon;
    daemon = MHD_start_daemon(MHD_USE_SELECT_INTERNALLY, 8080, NULL, NULL, &http_hello_page, NULL, MHD_OPTION_END);
    if (daemon == NULL) {
        return 1;
    }

    printf("Server running on port 8080. Press Enter to exit.\n");
    getchar();

    MHD_stop_daemon(daemon);
    return 0;
}
