# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import urllib

__addon__               = xbmcaddon.Addon()
__addon_id__            = __addon__.getAddonInfo('id')
__addonname__           = __addon__.getAddonInfo('name')
__icon__                = __addon__.getAddonInfo('icon')
__addonpath__           = xbmc.translatePath(__addon__.getAddonInfo('path'))
__lang__                = __addon__.getLocalizedString

class PlayTrailer:
    
    def __init__(self):
    
        self.getTrailer()
    
    def getTrailer(self):
    
        trailer = xbmc.getInfoLabel('ListItem.Trailer')
        if 'plugin://plugin.video.youtube' not in trailer:
            trailer = urllib.quote(trailer).replace('%3A', ':')
        
        if len(trailer) > 0:
            xbmc.Player().play(trailer)
        else:
            self.notify(__lang__(32000))
            return
            
    def notify(self, msg):
        if 'true' in __addon__.getSetting('notify'):
            xbmc.executebuiltin('Notification(' + __addonname__ + ', ' + msg.encode('utf-8') + ', 4000, ' + __icon__ + ')')
        
PlayTrailer()