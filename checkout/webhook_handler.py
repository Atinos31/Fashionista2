from djago.htttp import HttpResponse


class StripeWH_Handler:
    """ handles stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event[type]}',
            status=200
        )
