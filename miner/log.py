#logging function
#
def log(message, level):
  '''Conditionally write a message to stdout based on command line options and level.'''
#
  global DEBUG
  global DEBUG_PROTOCOL
  global QUIET
#
  if QUIET and level != LEVEL_ERROR: return
  if not DEBUG_PROTOCOL and level == LEVEL_PROTOCOL: return
  if not DEBUG and level == LEVEL_DEBUG: return
#
  if level != LEVEL_PROTOCOL: message = '[%s] %s' % (level.upper(), message)
#
  print ("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), message))
