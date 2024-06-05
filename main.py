from gradio_interfaces import iface


def start_service():
    iface.launch(inbrowser=True, server_name='0.0.0.0')


if __name__ == "__main__":
    start_service()
