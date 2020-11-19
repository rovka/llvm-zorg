from buildbot.process.properties import Interpolate
from buildbot.plugins import reporters

import config
from zorg.buildbot.util.InformativeMailNotifier import LLVMInformativeMailNotifier

# Returns a list of Status Targets. The results of each build will be
# pushed to these targets. buildbot.plugins reporters has a variety
# to choose from, including email senders, and IRC bots.
def getReporters():
#    if config.options.getboolean('Master Options', 'is_production'):
#        return all
#    else:
    # Staging buildbot does not report issues.
    return []
