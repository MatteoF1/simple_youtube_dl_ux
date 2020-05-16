import youtube_dl
from PyQt5.QtWidgets import QWidget, QFormLayout, QPushButton, QLineEdit, QApplication
from sys import exit, argv

''' Youtube DL UX '''
class Youtube_DL(QWidget):

    '''Initialization'''
    def __init__(self):
        super().__init__()

        # configuring layout
        self.__layout = QFormLayout()
        
        # configuring button to start the download
        self.__send_button = QPushButton('Start', self)
        self.__send_button.setCheckable(True)

        # connect the button to the method that manages the click event
        self.__send_button.clicked[bool].connect(self._start_download)

        # configuring input element
        self.__input = QLineEdit()

        self.__layout.addRow('Insert the link to the song: ', self.__input)
        self.__layout.addRow('Download: ', self.__send_button)
        
        # configuring window
        self.setLayout(self.__layout)
        self.setWindowTitle("Youtube Download")

    '''Starting download of music record'''
    def _start_download(self):
        ''' extracting youtube internal link to avoid extra URL parameters '''
        if self.__input.text():
            start_internal_link_index = self.__input.text().find('?') + 1
            end_internal_link_index = self.__input.text().find('&', start_internal_link_index)
            internal_link = self.__input.text()[start_internal_link_index : end_internal_link_index if end_internal_link_index != -1 else len(self.__input.text())]
            print('Downloading: ' + 'https://www.youtube.com/watch?%s' % internal_link)        
            
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
    
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(['https://www.youtube.com/watch?%s' % internal_link])
        self.close()

if __name__ == '__main__':
    app = QApplication(argv)
    this_download = Youtube_DL()
    this_download.show()
    exit(app.exec_())
