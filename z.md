# vhost

Script para automatizar a gestão de hosts virtuais no servidor apache.
O comando `vhost` edita os arquivos necessários e reinicia o servidor apache.



```Bash
$ vhost {{DocumentRoot}} {{ServerName}} {{Port}}
```

DocumentRoot - Caminho da pasta que será servida
ServerName - Alias do virtual host
Port - Porta usada para o acesso

Editar o arquivo `httpd-vhosts.conf` 

```Apache
<VirtualHost {{ServerName}}:80>
    DocumentRoot "{{DocumentRoot}}"
    ServerName {{ServerName}}
    ErrorLog "/usr/local/var/log/httpd/{{ServerName}}-error_log"
    CustomLog "/usr/local/var/log/httpd/{{ServerName}}-access_log" combined
    <Directory "{{DocumentRoot}}">
        Require all granted
    </Directory>
</VirtualHost>
```

<!-- `/etc/apache2/sites-enabled` -->

Editar o arquivo `/etc/hosts`

```Apache
###
#
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
#
###

127.0.0.1	localhost hacker outronomequalquer
127.0.0.1	v1.com www.v1.com
127.0.0.1	usaressepadrao.com www.usaressepadrao.com
127.0.0.1	{{ServerName}} www.{{ServerName}}
255.255.255.255	broadcasthost
::1             localhost
```

## Adicionar vhost


## Alterar ServerName


## Excluir vhost


```Bash
$ vhost -rm {{ServerName}}
```
## Referências

