# INTEGRANTES:
# MERO SARCOS CAROLINE THALIA
# QUIÑONEZ JAIME SERGIO AURELIO
# QUIÑONEZ RONQUILLO ODALYS RAQUEL

import sys

from PySide6.QtWidgets import QApplication

from servicio.persona_principal import PersonaPrincipal

app = QApplication()
vtn_principal: PersonaPrincipal = PersonaPrincipal()
vtn_principal.show()
sys.exit(app.exec())




