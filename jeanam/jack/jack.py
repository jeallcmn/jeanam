# import logging
# import jack

# class JackClient(object):
#     """
#     Based in: http://jackclient-python.readthedocs.io/en/0.4.2/examples.html#chatty-client

#     Through the :class:`jack.JackClient` it is possible to be notified when `x-run`
#     occurs and when the Jack server is closed::

#         >>> client = JackClient()
#         >>> client.xrun_callback = lambda delay: print('x-run', delay)
#         >>> client.shutdown_callback = lambda status, reason: print('shutdown: ', status, reason)

#     When you don't use anymore, close it::

#         >>> client.close()

#     :param bool no_start_server: False if starts a new JACK server
#                                  True if uses a already started jack (ex: using `jackdump`)
#     :param name: Jack client name. Default: `JackClient`
#     """
#     def __init__(self, no_start_server=True, name='JackClient', xrun_callback=lambda delay: ..., shutdown=lambda status, reason: ...):
#         self.client = jack.Client(name=name, no_start_server=no_start_server)

#         self.xrun_callback = xrun_callback
#         self.shutdown_callback = shutdown

#         # if self.client.status.server_started:
#         #     logging.info('JACK server was started')
#         # else:
#         #     logging.info('JACK server was already running')

#         # if self.client.status.name_not_unique:
#         #     logging.info('Unique client name generated {}'.format(self.client.name))

#         self.client.activate()

#     def audio_inputs(self):
#         return self.client.get_ports(is_audio=True, is_physical=True, is_input=True)
#     def audio_outputs(self):
#         return self.client.get_ports(is_audio=True, is_physical=True, is_output=True)
#     def midi_inputs(self):
#         return self.client.get_ports(is_midi=True, is_physical=True, is_input=True)
#     def midi_outputs(self):
#         return self.client.get_ports(is_midi=True, is_physical=True, is_output=True)
#     def close(self):
#         self.client.deactivate()
#         self.client.close()
