# Backing up the Database #

Applicant currently uses Postgresql for the database.  Here is a simple process
to backup the data in production.

1. Review the documentation at: https://www.postgresql.org/docs/devel/static/app-pgdump.html
2. ssh into the remote server (jobs.harenconstruction.com).  The ssh config
   settings for hereafter define thee host as applicant.
3. The command to use to create a backup of the database is:

        root@applicant:~# pg_dump -h localhost -Fc -o -U applicant applicant > /root/backups/applicant.dump

4. This uses pg_dump to connect to localhost (where the postgresql server resides), and dump using
  a custom output format (-Fc) compressed and suitable for importing, while preserving foreign
  key ids (-o) using the user applicant (-U) to connect to the database applicant, then save the
  resulting output to /root/backups/applicant.dump.  

5. To restore, inside vagrant:

        (env) vagrant@vagrant:/vagrant/local$ sudo -u postgres pg_restore -C -d applicant applicant.dump
