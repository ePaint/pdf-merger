import os
from dataclasses import dataclass


@dataclass
class Settings:
    page_number_format: str = 'Página [PAGE_NUMBER] de [TOTAL_PAGES]'
    input_folder: str = 'Input'
    output_folder: str = 'Output'

    # DO NOT MODIFY THIS ATTRIBUTE
    # This is the path to the root of the project, which is the parent directory of the Settings folder
    _project_location: str = os.path.dirname(os.path.abspath(__file__).replace('Settings', ''))

    @property
    def input_path(self) -> str:
        return os.path.join(self._project_location, self.input_folder)

    @property
    def output_path(self) -> str:
        return os.path.join(self._project_location, self.output_folder)


SETTINGS = Settings()
