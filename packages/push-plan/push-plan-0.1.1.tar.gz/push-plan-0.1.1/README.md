# push-plan: Finger.farm status updater
Program to archive `~/plan` & `~/project` files and push their latest content to finger.farm finger
hosting service.

## Usage
Copy `doc/sample-config.toml` as `~/.config/push-plan/config.toml`. Modify values appropriately,
especially user name and API token command. Default config uses `gopass` to access the credential.

Create plan and project file as specified in the config file. Modify them as required. Use the 
command thereafter as follows:

```
usage: push-plan [-h] [--no-save] [--no-push] [--skip-check] [-d]

Record and update finger status

options:
  -h, --help    show this help message and exit
  --no-save     Don't save status. Push previously saved status.
  --no-push     Don't push status.
  --skip-check  Skip check for change in status.
  -d, --debug   Print config info for debugging
```

The files will be backed up in the specified archive directory prior to uploading online.

## Development
Development happens over [sourcehut](https://sr.ht/~gokuldas/push-plan/). Discussion and
collaboration are over [~gokuldas/projects mailing list](mailto:~gokuldas/projects@lists.sr.ht).
Task and bug tracking is done on [dedicated tracker](https://todo.sr.ht/~gokuldas/push-plan).

## License
Copyright (C) 2022 Gokul Das B

This program is distributed under GPLv3 license. Refer LICENSE file for details.
