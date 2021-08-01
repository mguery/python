#!/usr/bin/env python
import ldclient
from ldclient.config import Config

# Set sdk_key to your LaunchDarkly SDK key before running
sdk_key = "sdk-here-####"

# Set feature_flag_key to the feature flag key you want to evaluate
feature_flag_key = "my-boolean-flag"

def show_message(s):
  print("*** %s" % s)
  print()

if __name__ == "__main__":
  if not sdk_key:
    show_message("Please edit test.py to set sdk_key to your LaunchDarkly SDK key first")
    exit()

  ldclient.set_config(Config(sdk_key))


  if ldclient.get().is_initialized():
    show_message("SDK successfully initialized!")
  else:
    show_message("SDK failed to initialize")
    exit()


  user = {
    "key": "example-user-key",
    "name": "Sandy",
    "email": "email@google.com"
  }

  flag_value = ldclient.get().variation(feature_flag_key, user, False)

  show_message("Feature flag '%s' is %s for this user" % (feature_flag_key, flag_value))

  ldclient.get().close()
