# Dynamics Group Bot

Beep boop.


### Notes

If you update any of the data in `secrets`, you have to re-tar and gzip it, then gpg encrypt it with:

   gpg -c secrets.tar.gz


And add the GPG passphrase to GitHub actions as a repository secret environment
variable `$GPG_PASSPHRASE`.

Each semester, make sure to update the `DATES` file to contain a list of dates for the
Galactic Dynamics community meetings.
