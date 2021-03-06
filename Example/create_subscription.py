import sys
import argparse
sys.path.insert(0,'../')
from ThingPlugApi import ThingPlug 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'ThingPlug Login Example')
    
    parser.add_argument('-u', '--user_id', type=str, help='ThingPlug User ID', required=True)
    parser.add_argument('-p', '--user_pw', type=str, help='ThingPlug User Password', required=True)
    parser.add_argument('-n', '--node_id', type=str, help='ThingPlug Node ID', required=True)
    parser.add_argument('-c', '--container', type=str, help='ThingPlug Container Name', required=True)
    parser.add_argument('-s', '--subscription', type=str, help='ThingPlug Container Name', required=True)
    parser.add_argument('-nu', '--notification_uri', type=str, help='ThingPlug Notification URI', required=True)
    
    args = parser.parse_args()
    
    thingplug = ThingPlug.ThingPlug('onem2m.sktiot.com',9443)
    thingplug.login(args.user_id, args.user_pw)
    
    thingplug.createSubscription( args.node_id, args.subscription, args.container, args.notification_uri )
