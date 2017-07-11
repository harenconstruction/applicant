# Backing up the Files #

The actual application code, which you would update using git, is stored under:

        /home/applicant/applicant

Resumes are referenced under:

        /home/applicant/media/resumes/

Both of these directories should be backed up before updating production.  If
working on development, you likely only need media or a database dump. To create
a backup of the two directories:

        cd /home/applicant
        tar czvf applicant.tar.gz applicant
        tar czvf applicant-media.tar.gz media
        mv applicant.tar.gz /root/backups/
        mv applicant-media.tar.gz /root/backups/

Finally, copy these files to your local system or backup server:

        cd /path/to/local/backups
        scp applicant:/root/backups/applicant.tar.gz applicant.tar.gz
        scp applicant:/root/backups/applicant-media.tar.gz applicant-media.tar.gz
