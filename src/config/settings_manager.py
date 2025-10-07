from PySide6.QtCore import QSettings

class SettingsManager:
    def __init__(self, organization="GenBBS", application="GenBBS"):
        self.settings = QSettings(organization, application)
        self._default_settings = self._load_default_settings()
        self._apply_default_settings_if_missing()

    def _load_default_settings(self):
        # Define your default settings here.
        # These will be used if no user-specific setting is found.
        return {
            "reinforcement/auto_fill_values": False,
            "reinforcement/auto_generate_bar_mark": False,
            "reinforcement/allow_keyboard_shortcuts": False,
            "reinforcement/no_of_bars": "10",
            "reinforcement/dimension_a": "100",
            "reinforcement/dimension_b": "100",
            "reinforcement/dimension_c": "100",
            "reinforcement/dimension_d": "100",
            "reinforcement/dimension_e": "100",
            "reinforcement/dimension_f": "100",
            "reinforcement/dimension_r": "100",
            "reinforcement/bar_size": "10", # Default bar size
            "reinforcement/shape_code": "00", # Default shape code
        }

    def _apply_default_settings_if_missing(self):
        for key, value in self._default_settings.items():
            if not self.settings.contains(key):
                self.settings.setValue(key, value)
        self.settings.sync() # Ensure defaults are written if not present

    def get_setting(self, key, default_value=None):
        if default_value is None:
            default_value = self._default_settings.get(key)
        return self.settings.value(key, default_value)

    def set_setting(self, key, value):
        self.settings.setValue(key, value)
        # self.settings.sync() # Optional: force immediate write if needed for critical settings