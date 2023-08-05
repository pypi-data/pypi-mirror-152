import os
from typing import Dict, List, Optional, Tuple

from qtpy.QtWidgets import (
    QButtonGroup,
    QCheckBox,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QRadioButton,
    QVBoxLayout,
    QWidget,
)

from napari.errors import ReaderPluginError
from napari.plugins.utils import get_potential_readers
from napari.settings import get_settings

from ...utils.translations import trans


class QtReaderDialog(QDialog):
    """Dialog for user to select a reader plugin for a given file extension or folder"""

    def __init__(
        self,
        pth: str = '',
        parent: QWidget = None,
        readers: Dict[str, str] = {},
        error_message: str = '',
    ):
        super().__init__(parent)
        self.setObjectName('Choose reader')
        self.setWindowTitle(trans._('Choose reader'))
        self._current_file = pth

        if os.path.isdir(pth) and str(pth).endswith('/'):
            pth = os.path.dirname(pth)
        self._extension = os.path.splitext(pth)[1]

        self._reader_buttons = []
        self.setup_ui(error_message, readers)

    def setup_ui(self, error_message, readers):
        """Build UI using given error_messsage and readers dict"""

        # add instruction label
        layout = QVBoxLayout()
        if error_message:
            error_message += "\n"
        label = QLabel(
            f"{error_message}Choose reader for {self._current_file}:"
        )
        layout.addWidget(label)

        # add radio button for each reader plugin
        self.reader_btn_group = QButtonGroup(self)
        self.add_reader_buttons(layout, readers)
        if self.reader_btn_group.buttons():
            self.reader_btn_group.buttons()[0].toggle()

        # OK & cancel buttons for the dialog
        btns = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.btn_box = QDialogButtonBox(btns)
        self.btn_box.accepted.connect(self.accept)
        self.btn_box.rejected.connect(self.reject)

        # checkbox to remember the choice (doesn't pop up for folders with no extension)
        if self._extension:
            self.persist_checkbox = QCheckBox(
                f'Remember this choice for files with a {self._extension} extension'
            )
            self.persist_checkbox.toggle()
            layout.addWidget(self.persist_checkbox)

        layout.addWidget(self.btn_box)
        self.setLayout(layout)

    def add_reader_buttons(self, layout, readers):
        """Add radio button to layout for each reader in readers"""
        for display_name in sorted(readers.values()):
            button = QRadioButton(f"{display_name}")
            self.reader_btn_group.addButton(button)
            layout.addWidget(button)

    def _get_plugin_choice(self):
        """Get user's plugin choice based on the checked button"""
        checked_btn = self.reader_btn_group.checkedButton()
        if checked_btn:
            return checked_btn.text()

    def _get_persist_choice(self):
        """Get persistence checkbox choice"""
        return (
            hasattr(self, 'persist_checkbox')
            and self.persist_checkbox.isChecked()
        )

    def get_user_choices(self) -> Tuple[str, bool]:
        """Execute dialog and get user choices"""
        display_name = ''
        persist_choice = False

        dialog_result = self.exec_()
        # user pressed cancel
        if dialog_result:
            # grab the selected radio button text
            display_name = self._get_plugin_choice()
            # grab the persistence checkbox choice
            persist_choice = self._get_persist_choice()
        return display_name, persist_choice


def handle_gui_reading(
    paths: List[str],
    qt_viewer,
    stack: bool,
    plugin_name: Optional[str] = None,
    error: Optional[ReaderPluginError] = None,
):
    """Present reader dialog to choose reader and open paths based on result.

    This function is called whenever ViewerModel._open_or_get_error returns
    an error from a GUI interaction e.g. dragging & dropping a file or using
    the File -> Open dialogs. It prepares remaining readers and error message
    for display, opens the reader dialog and based on user entry opens
    paths using the chosen plugin. Any errors raised in the process of reading
    with the chosen plugin are reraised.

    Parameters
    ----------
    _paths : list[str]
        list of paths to open, as strings
    viewer : QtViewer
        QtViewer to associate dialog with
    stack : bool
        True if list of paths should be stacked, otherwise False
    plugin_name : str | None
        name of plugin already tried, if any
    error : ReaderPluginError | None
        previous error raised in the process of opening
    """
    _path = paths[0]
    readers = prepare_remaining_readers(paths, plugin_name, error)
    error_message = str(error) if error else ''

    readerDialog = QtReaderDialog(
        parent=qt_viewer,
        pth=_path,
        error_message=error_message,
        readers=readers,
    )
    display_name, persist = readerDialog.get_user_choices()
    if display_name:
        open_with_dialog_choices(
            display_name,
            persist,
            readerDialog._extension,
            readers,
            paths,
            stack,
            qt_viewer,
        )


def prepare_remaining_readers(
    paths: List[str],
    plugin_name: Optional[str] = None,
    error: Optional[ReaderPluginError] = None,
):
    """Remove tried plugin from readers and raise error if no readers remain.

    Parameters
    ----------
    paths : List[str]
        paths to open
    plugin_name : str | None
        name of plugin previously tried, if any
    error : ReaderPluginError | None
        previous error raised in the process of opening

    Returns
    -------
    readers: Dict[str, str]
        remaining readers to present to user

    Raises
    ------
    ReaderPluginError
        raises previous error if no readers are left to try
    """
    readers = get_potential_readers(paths[0])
    # remove plugin we already tried e.g. prefered plugin
    if plugin_name in readers:
        del readers[plugin_name]
    # if there's no other readers left, raise the exception
    if not readers and error:
        raise ReaderPluginError(
            trans._(
                "Tried to read {path_message} with plugin {plugin}, because it was associated with that file extension/because it is the only plugin capable of reading that path, but it gave an error. Try associating a different plugin or installing a different plugin for this kind of file.",
                path_message=f"[{paths[0]}, ...]"
                if len(paths) > 1
                else paths[0],
                plugin=plugin_name,
            ),
            plugin_name,
            paths,
        ) from error

    return readers


def open_with_dialog_choices(
    display_name: str,
    persist: bool,
    extension: str,
    readers: Dict[str, str],
    paths: List[str],
    stack: bool,
    qt_viewer,
):
    """Open paths with chosen plugin from reader dialog, persisting if chosen.

    Parameters
    ----------
    display_name : str
        display name of plugin to use
    persist : bool
        True if user chose to persist plugin association, otherwise False
    extension : str
        file extension for association of preferences
    readers : Dict[str, str]
        plugin-name: display-name dictionary of remaining readers
    _paths : List[str]
        paths to open
    stack : bool
        True if files should be opened as a stack, otherwise False
    qt_viewer : QtViewer
        viewer to add layers to
    """
    # TODO: disambiguate with reader title
    plugin_name = [
        p_name for p_name, d_name in readers.items() if d_name == display_name
    ][0]
    # may throw error, but we let it this time
    qt_viewer.viewer._add_layers_with_plugins(
        paths, stack=stack, plugin=plugin_name
    )

    if persist:
        get_settings().plugins.extension2reader = {
            **get_settings().plugins.extension2reader,
            f'*{extension}': plugin_name,
        }
