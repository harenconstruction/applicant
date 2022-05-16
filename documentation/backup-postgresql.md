# Database Backups #

The applicant project uses postgresql. 

# Backing up the Live Database #

Here is a simple process to backup the data in production.

1. Review the documentation at: https://www.postgresql.org/docs/devel/static/app-pgdump.html
2. ssh into the remote server (www.harenconstruction.com).  The ssh config
   settings for hereafter define thee host as applicant.
3. The command to use to create a backup of the database is:

        root@applicant:~# pg_dump -h localhost -Fc -o -U applicant applicant > /root/backups/applicant.dump

4. This uses pg_dump to connect to localhost (where the postgresql server resides), and dump using
  a custom output format (-Fc) compressed and suitable for importing, while preserving foreign
  key ids (-o) using the user applicant (-U) to connect to the database applicant, then save the
  resulting output to /root/backups/applicant.dump.  

## Restore ##

Here we document the specific steps we may take to restore a backup, in vagrant,
staging, and eventually in production (we hope we never need that).

### Vagrant ###

To restore, inside vagrant:

        (env) vagrant@vagrant:/vagrant/local$ sudo -u postgres pg_restore -C -d applicant applicant.dump

### Staging ###

1. First delete the database:

        $ dropdb -U applicant -h 127.0.0.1 applicant

If this command fails, you may need to stop postgresql due to open connections.

        $ sudo service postgresql stop
        $ sudo service postgresql start
        $ dropdb -U applicant -h 127.0.0.1 applicant

2. Now recreate the database:

        $ sudo -u postgres createdb -E UTF8 -T template0 --locale=en_US.utf8 applicant -O applicant

        $ sudo -u postgres psql -c "CREATE DATABASE applicant ENCODING = 'UTF-8' LC_CTYPE = 'en_US.UTF-8' LC_COLLATE = 'en_US.UTF-8' OWNER applicant TEMPLATE template0"

3. Finally, import the raw/text sql dump:

        $ psql -U applicant -h 127.0.0.1 applicant < applicant.sql

        Alternatively, if the dump was using PostgreSQL's custom-format dump:

        $ pg_restore -U applicant -h 127.0.0.1 -d applicant /path/to/applicant.dump 
        