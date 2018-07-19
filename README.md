Role Name
=========

Install certbot ssl certs, configure for nginx

Requirements
------------

Role Variables
--------------

These must be set or the role will error:

    certbot_hostname: my.domain.com
    certbot_admin_email: me@domain.com

Optional configs:

    certbot_auto_renew: yes
    certbot_script: /opt/certbot-auto
    certbot_live_dir: '/etc/letsencrypt/live/{{ certbot_hostname }}'
  
Dependencies
------------

Example Playbook
----------------

    - hosts: servers
      - import_role:
          name: certbot
        vars:
            certbot_hostname: my.domain.com
            certbot_admin_email: me@domain.com
