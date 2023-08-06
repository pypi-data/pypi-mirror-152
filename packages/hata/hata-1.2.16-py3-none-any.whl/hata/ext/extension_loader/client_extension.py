__all__ = ()

from scarletio import KeepType

from ...discord.client import Client

from .extension import EXTENSIONS, EXTENSION_STATE_LOADED


@KeepType(Client)
class Client:

    @property
    def extensions(self):
        """
        Returns a list of extensions added to the client. Added by the `extension_loader` extension.
        
        Returns
        -------
        extensions : `list` of ``Extension``
        """
        extensions = []
        for extension in EXTENSIONS.values():
            if extension._state == EXTENSION_STATE_LOADED:
                snapshot_difference = extension._snapshot_difference
                if (snapshot_difference is not None):
                    for snapshot in snapshot_difference:
                        if (snapshot.client is self) and snapshot_difference:
                            extensions.append(extension)
                            break
        
        return extensions
