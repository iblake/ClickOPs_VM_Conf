# Oracle Agent Filesystem GitOps

Este repositorio contiene la configuración necesaria para crear un sistema de archivos en `/opt/oracle/agent` en una VM de OCI utilizando Ansible y GitHub Actions.

## Cómo utilizar

1. Crea un fork de este repositorio
2. Actualiza el archivo `config/fs_config.yml` con los valores deseados:
   - `oracle_agent_fs_size`: Tamaño del sistema de archivos (ej: "10g", "500m")
   - `oracle_agent_fs_type`: Tipo de sistema de archivos (ej: "xfs", "ext4")
   - `oracle_agent_vg`: Grupo de volúmenes existente
   - `oracle_agent_lv`: Nombre del volumen lógico a crear
3. Crea un Pull Request con los cambios
4. Una vez aprobado y fusionado el PR, GitHub Actions ejecutará automáticamente el playbook de Ansible para crear el sistema de archivos

## Requisitos

- VM en OCI con acceso SSH
- Grupo de volúmenes existente con espacio disponible
- Credenciales de OCI configuradas como secretos en GitHub:
  - `OCI_CONFIG`: Contenido del archivo de configuración de OCI
  - `OCI_PRIVATE_KEY`: Clave privada para acceder a OCI
  - `OCI_INSTANCE_IP`: Dirección IP de la instancia destino