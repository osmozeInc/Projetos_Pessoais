import os
import subprocess

os.system('pip list')
package = subprocess.run(['pip', 'list'], capture_output=True, text=True)
indice = package.stdout.find('-\n')
package_apagar = package.stdout[indice + 1:].split()
for i in range(len(package_apagar)):
    if i % 2 == 0 and package_apagar[i] != 'pip':
        os.system(f'pip uninstall -y {package_apagar[i]}')

# Este programa lista todos os pacotes instalados e depois os desinstala, com exxceção do pip.
