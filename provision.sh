#!/bin/sh

if [ ! -e "/home/vagrant/provisioned" ]
then
    echo "set grub-pc/install_devices /dev/sda" | debconf-communicate
    apt-get update
    apt-get -y upgrade
    apt-get -y install supervisor unzip git python3 python3-dev python3-setuptools libjpeg-dev python3-pip python-virtualenv postgresql libpq-dev

    sudo -u postgres createuser --no-superuser --no-createdb --no-createrole applicant || exit 1
    sudo -u postgres psql -c "alter user applicant password 'applicant'"
    sudo -u postgres createdb applicant -O applicant || exit 1

    # Install the virtualenv in ~vagrant but the project in /vagrant.
    sudo -u vagrant -s <<'EOF' || exit 1
virtualenv -p /usr/bin/python3.5 /home/vagrant/env
source /home/vagrant/env/bin/activate
cd /vagrant/
pip install -r requirements.txt
cd /vagrant/applicant
/home/vagrant/env/bin/python manage.py migrate || exit 1
/home/vagrant/env/bin/python manage.py loaddata developerdata || exit 1
EOF

    cat <<'EOF' > /etc/supervisor/conf.d/runserver.conf
[program:runserver]
command=/home/vagrant/env/bin/python manage.py runserver 0.0.0.0:8000
directory=/vagrant/applicant_project
autostart=0
EOF
    supervisorctl reload || exit 1

    touch /home/vagrant/provisioned
fi

supervisorctl start runserver
