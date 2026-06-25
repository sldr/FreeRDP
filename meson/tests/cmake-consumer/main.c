/* Minimal consumer: include public headers and reference symbols from each
 * imported library, exercising both the INTERFACE_INCLUDE_DIRECTORIES and the
 * link interface of the Meson-generated CMake package targets. */
#include <winpr/winpr.h>
#include <winpr/library.h>
#include <freerdp/freerdp.h>
#include <freerdp/client.h>

int main(void)
{
	RDP_CLIENT_ENTRY_POINTS entry = { 0 };
	rdpContext* context = NULL;

	entry.Size = sizeof(entry);
	entry.Version = RDP_CLIENT_INTERFACE_VERSION;

	context = freerdp_client_context_new(&entry);
	if (context)
		freerdp_client_context_free(context);

	return 0;
}
