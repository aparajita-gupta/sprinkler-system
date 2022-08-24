//
//  Schedule.swift
//  SprinklerSystem
//
//  Created by Aparajita Gupta on 8/17/22.
//

import UIKit

class Schedule: UIViewController {

    @IBOutlet weak var dayTextField: UITextField!
   // @IBOutlet var dayPicker: UIPickerView!
    
    let dayOptions = ["Every Sunday", "Every Monday", "Every Tuesday", "Every Wednesday", "Every Thursday", "Every Friday", "Every Saturday", "Every Weekday", "Every Weekend"]
    
    var pickerView = UIPickerView()
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        pickerView.delegate = self
        pickerView.dataSource = self
        
        dayTextField.inputView = pickerView
        dayTextField.textAlignment = .center
        
        //dayPicker.delegate = self
        //dayPicker.dataSource = self
        
    }
    

}
    extension Schedule: UIPickerViewDelegate, UIPickerViewDataSource {
        
        func numberOfComponents(in pickerView: UIPickerView) -> Int {
            return 1
        }
        func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
            return dayOptions.count
        }
        
        func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
            return dayOptions[row]
        }
        func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
            dayTextField.text = dayOptions[row]
            dayTextField.resignFirstResponder()
            
        }
        
    }
