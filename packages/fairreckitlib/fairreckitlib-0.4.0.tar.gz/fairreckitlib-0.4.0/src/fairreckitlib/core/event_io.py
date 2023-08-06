"""This module contains all event ids and callback functions that are IO related.

Constants:

    ON_MAKE_DIR: id of the event that is used when a directory is created.
    ON_REMOVE_DIR: id of the event that is used when a directory is removed.
    ON_REMOVE_FILE: id of the event that is used when a file is removed.
    ON_RENAME_FILE: id of the event that is used when a file is renamed.

Functions:

    on_make_dir: call when a directory is created.
    on_remove_dir: call when a directory is removed.
    on_remove_file: call when a file is removed.
    on_rename_file: call when a file is renamed.

This program has been developed by students from the bachelor Computer Science at
Utrecht University within the Software Project course.
© Copyright Utrecht University (Department of Information and Computing Sciences)
"""

from typing import Any, Callable, List, Tuple

ON_MAKE_DIR = 'IO.on_make_dir'
ON_REMOVE_DIR = 'IO.on_remove_dir'
ON_REMOVE_FILE = 'IO.on_remove_file'
ON_RENAME_FILE = 'IO.on_rename_file'


def get_io_events() -> List[Tuple[str, Callable[[Any], None]]]:
    """Get all IO events.

    The Call backs are specified below and serve as a default
    implementation for the RecommenderSystem class including the keyword arguments
    that are available.

    Returns:
        a list of pairs in the format (event_id, func_on_event)
    """
    return [
        (ON_MAKE_DIR, on_make_dir),
        (ON_REMOVE_DIR, on_remove_dir),
        (ON_REMOVE_FILE, on_remove_file),
        (ON_RENAME_FILE, on_rename_file)
    ]


def on_make_dir(event_listener: Any, **kwargs) -> None:
    """Call back when a new directory is created.

    Args:
        event_listener: the listener that is registered
            in the event dispatcher with this callback.

    Keyword Args:
        dir(str): the path of the directory that was created.
    """
    if event_listener.verbose:
        print('Creating directory:', kwargs['dir'])


def on_remove_dir(event_listener: Any, **kwargs) -> None:
    """Call back when an existing directory is removed.

    Args:
        event_listener: the listener that is registered
            in the event dispatcher with this callback.

    Keyword Args:
        dir(str): the path of the directory that was removed.
    """
    if event_listener.verbose:
        print('Removing directory:', kwargs['dir'])


def on_remove_file(event_listener: Any, **kwargs) -> None:
    """Call back when an existing file is removed.

    Args:
        event_listener: the listener that is registered
            in the event dispatcher with this callback.

    Keyword Args:
        file(str): the path of the file that was removed.
    """
    if event_listener.verbose:
        print('Removing file:', kwargs['file'])


def on_rename_file(event_listener: Any, **kwargs) -> None:
    """Call back when an existing file is renamed.

    Args:
        event_listener: the listener that is registered
            in the event dispatcher with this callback.

    Keyword Args:
        src_file(str): the path of the file before renaming.
        dst_file(str): the path of the file after renaming.
    """
    if event_listener.verbose:
        print('Renaming file:', kwargs['src_file'], 'to', kwargs['dst_file'])
