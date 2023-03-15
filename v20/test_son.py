#test_son

import os
import audioop
cwd = os.getcwd()
cwd = cwd.replace("\\", "/" )
cwd = cwd+str("/")


file = str(cwd)+"assets/musica/Gymnopédie No°1.wav"
os.system("mpg123 " + file)