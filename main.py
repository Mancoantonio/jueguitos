import sys
import os
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QTimer



class SpriteWindow(QLabel):
    def __init__(self, folder, fps=12, speed=2):
        super().__init__()

        # cargar frames
        folder = "sprites"

        self.frames = []
        for f in sorted(os.listdir(folder)):
            if f.lower().endswith((".png", ".gif")):
                pix = QPixmap(os.path.join(folder, f))
                pix = pix.scaled(pix.width()*1.3, pix.height()*1.3)  # factor, puede cambiar
                self.frames.append(pix)

        self.frame_index = 0
        self.speed = speed
        self.dir = 1  # 1 derecha, -1 izquierda

        # configurar ventana
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setPixmap(self.frames[0])
        self.resize(self.frames[0].size())

        # posición inicial
        self.move(100, 100)

        # animación
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_sprite)
        self.timer.start(int(1000 / fps))

    def update_sprite(self):
        # cambiar frame
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.setPixmap(self.frames[self.frame_index])

        # mover horizontal
        x = self.x() + self.speed * self.dir
        y = self.y()

        # bordes de pantalla
        screen = QApplication.primaryScreen().geometry()
        y = screen.height() - self.height() - 40
        if x < 0:
            x = 0
            self.dir = 1
        elif x + self.width() > screen.width():
            x = screen.width() - self.width()
            self.dir = -1

        self.move(x, y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    sprite = SpriteWindow(folder="sprites")   # carpeta con tus frames
    sprite.show()
    sys.exit(app.exec())