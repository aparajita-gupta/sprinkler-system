//
//  SetSchedule.swift
//  SprinklerSystem
//
//  Created by Uttam Gupta on 8/20/22.
//

import UIKit

class SetSchedule: UIViewController {

    @IBOutlet var dayPicker: UIPickerView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        dayPicker.delegate = self
        dayPicker.dataSource = self

        // Do any additional setup after loading the view.
        }
                
    }
extension SetSchedule: UIPickerViewDataSource {
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return 10
    }
    
    
}

extension SetSchedule: UIPickerViewDelegate {
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
         return "test"
    }
    
}
