//
//  ViewController.swift
//  SprinklerSystem
//
//  Created by Aparajita Gupta on 7/22/22.
//

import UIKit
import SwiftMQTT

class ViewController: UIViewController {
    var mqttSession: MQTTSession!
    @IBOutlet var z1Switch: UISwitch!
    @IBOutlet var z2Switch: UISwitch!
    @IBOutlet var z3Switch: UISwitch!
    @IBOutlet var z4Switch: UISwitch!
    let client = MqttClient()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        print("Load all")
            //z1Switch.setOn(true, animated: true)
                        
        // z1Switch.setValue(true, forKey: "sds")
        client.establishConnection()
       // client.publish(msg: "off", channel: "sprinkler")
        
        // Do any additional setup after loading the view.
    }
    
    @IBAction func z1switchDidChange(_ sender: UISwitch){
        if sender.isOn{
            print("On")
            client.publish(msg: "on", channel: "sprinkler/zone1")
        }
        else{
        print("Off")
            client.publish(msg: "off", channel: "sprinkler/zone1")
        }
    }
    
    @IBAction func z2switchDidChange(_ sender: UISwitch){
        if sender.isOn{
            print("On")
            client.publish(msg: "on", channel: "sprinkler/zone2")
        }
        else{
        print("Off")
            client.publish(msg: "off", channel: "sprinkler/zone2")
        }
    }
    
    @IBAction func z3switchDidChange(_ sender: UISwitch){
        if sender.isOn{
            print("On")
            client.publish(msg: "on", channel: "sprinkler/zone3")
        }
        else{
        print("Off")
            client.publish(msg: "off", channel: "sprinkler/zone3")
        }
    }
    
    @IBAction func z4switchDidChange(_ sender: UISwitch){
        if sender.isOn{
            print("On")
            client.publish(msg: "on", channel: "sprinkler/zone4")
        }
        else{
        print("Off")
            client.publish(msg: "off", channel: "sprinkler/zone4")
        }
    }


}

