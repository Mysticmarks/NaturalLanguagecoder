import unittest
from unittest.mock import patch, MagicMock
import sys

# Define global mocks to be used by sys.modules patcher
mock_tk_module_for_setup = MagicMock(name='setup_mock_tk')
mock_ttk_module_for_setup = MagicMock(name='setup_mock_ttk')
modules_to_mock_for_setup = {
    'tkinter': mock_tk_module_for_setup,
    'tkinter.ttk': mock_ttk_module_for_setup
}

# Placeholders for patchers and imported modules/classes
sys_modules_patcher_module_level = None
nltk_download_patcher_module_level = None
CodeConverterApp_module_level = None
nltk_module_for_patching = None # To store the imported nltk module

def setUpModule():
    """Called once, before any tests in this module run."""
    global sys_modules_patcher_module_level, nltk_download_patcher_module_level
    global CodeConverterApp_module_level, nltk_module_for_patching

    sys_modules_patcher_module_level = patch.dict(sys.modules, modules_to_mock_for_setup)
    sys_modules_patcher_module_level.start()

    # Patch nltk.download before chatcoder (which imports nltk) is imported
    nltk_download_patcher_module_level = patch('nltk.download', MagicMock(return_value=True))
    nltk_download_patcher_module_level.start()

    # Import nltk module itself into a global for direct patching later
    import nltk as imported_nltk_module
    nltk_module_for_patching = imported_nltk_module

    # Import CodeConverterApp now. It will use the above imported_nltk_module if it also does 'import nltk'.
    from chatcoder import CodeConverterApp as imported_app
    CodeConverterApp_module_level = imported_app


def tearDownModule():
    """Called once, after all tests in this module have run."""
    if nltk_download_patcher_module_level:
        nltk_download_patcher_module_level.stop()
    if sys_modules_patcher_module_level:
        sys_modules_patcher_module_level.stop()

class TestCodeConverterAppSimplified(unittest.TestCase):

    def test_convert_to_code_logic(self):
        # Use patch.object to patch word_tokenize and pos_tag directly on the
        # nltk module object that was imported in setUpModule.
        with patch.object(nltk_module_for_patching, 'word_tokenize', MagicMock(return_value=['test', 'function'])) as mock_word_tokenize_arg, \
             patch.object(nltk_module_for_patching, 'pos_tag', MagicMock(return_value=[('test', 'VB'), ('function', 'NN')])) as mock_pos_tag_arg:

            # Arrange
            # NLTK mocks are set up by the with statement's patch.object

            try:
                app = CodeConverterApp_module_level()
            except Exception as e:
                self.fail(f"Failed to instantiate CodeConverterApp: {e}")

            app.input_entry = MagicMock(name='mock_input_entry')
            app.input_entry.get = MagicMock(return_value="test function")

            app.output_text = MagicMock(name='mock_output_text')
            app.output_text.delete = MagicMock()
            app.output_text.insert = MagicMock()

            # Act
            app.convert_to_code()

            # Assert
            mock_word_tokenize_arg.assert_called_once_with("test function")
            mock_pos_tag_arg.assert_called_once_with(['test', 'function'])
            app.output_text.insert.assert_called_once_with(mock_tk_module_for_setup.END, "test() function ")

if __name__ == '__main__':
    unittest.main()
