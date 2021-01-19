class HGException(Exception):
    """
    Base exception for all exceptions pymax will raise.
    """


class HGRpcException(HGException):
    """
    Exception for errors while communicating via XML-RPC.
    """
