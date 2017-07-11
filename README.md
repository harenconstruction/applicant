# applicant #

The admin and management application for Haren Construction Company's
job application form.

## Documentation ##

For full documentation, please read [here](documentation/index.md).

## Running ##

If on Linux or OSX, you can:

  $ cd /path/to/project
  $ vagrant up

Or if you want to start and refresh from scratch:

  $ cd /path/to/project
  $ ./vagrant-refresh.sh

After running, the site should be accessible at: http://127.0.0.1:8095/

## Admin Interface ###

When running with vagrant, the default admin interface is at:

    URL: http://127.0.0.1:8095/admin/
    Username: admin
    Password: applicant

Which is used to manage applications and applicants.

## Testing ##

If using the applicant-devops playbook script:

  $ vagrant up --no-provision

Then run the playbook as instructed.
