# Copying Backups #

The following general process should be used to copy the backups on the server
to your local system or backup server.  This should work in tandem with a cron
job which rotates and keeps a set of backups.

        cd /path/to/backups
        scp applicant:/root/backups/applicant.tar.gz applicant.tar.gz
        scp applicant:/root/backups/applicant-media.tar.gz applicant-media.tar.gz
        scp applicant:/root/backups/applicant.dump > applicant.dump
