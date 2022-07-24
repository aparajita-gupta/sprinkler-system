//
//  ViewController.swift
//  SprinklerSystem
//
//  Created by Aparajita Gupta on 7/22/22.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet var z1Switch: UISwitch!
    @IBOutlet var z2Switch: UISwitch!
    @IBOutlet var z3Switch: UISwitch!
    @IBOutlet var z4Switch: UISwitch!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    
    @IBAction func z1switchDidChange(_ sender: UISwitch){
        if sender.isOn{
          //  var zone1Status = "On"
        }
        else{
          //  var zone1Status = "Off"
        }
    }
    
    @IBAction func z2switchDidChange(_ sender: UISwitch){
        if sender.isOn{
          //  var zone2Status = "On"
        }
        else{
         //   var zone2Status = "Off"
        }
    }
    
    @IBAction func z3switchDidChange(_ sender: UISwitch){
        if sender.isOn{
         //   var zone3Status = "On"
        }
        else{
           // var zone3Status = "Off"
        }
    }
    
    @IBAction func z4switchDidChange(_ sender: UISwitch){
        if sender.isOn{
       //     var zone4Status = "On"
        }
        else{
        //    var zone4Status = "Off"
        }
    }


}

