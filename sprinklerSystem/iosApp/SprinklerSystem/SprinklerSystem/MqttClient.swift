//
//  MqttClient.swift
//  SprinklerSystem
//
//  Created by Aparajita Gupta on 7/24/22.
//

import Foundation
import SwiftMQTT



class MqttClient : MQTTSessionDelegate {
   
    
    var mqttSession: MQTTSession!
    
    func subscribeToChannel() {
            let channel = "sprinkler/status"
            mqttSession.subscribe(to: channel, delivering: .atLeastOnce) { (error) in
                if error == .none {
                    print("Subscribed to \(channel)")
                } else {
                    print("Error occurred during subscription:")
                    print(error.description)
                }
            }
        }
    func mqttDidReceive(message: MQTTMessage, from session: MQTTSession) {
            print("data received on topic \(message.topic) message \(message.stringRepresentation ?? "<>")")
        }

        func mqttDidDisconnect(session: MQTTSession, error: MQTTSessionError) {
            print("Session Disconnected.")
            if error != .none {
                print(error.description)
            }
        }

        func mqttDidAcknowledgePing(from session: MQTTSession) {
            print("Keep-alive ping acknowledged.")
        }
    func establishConnection() {
            let host = "192.168.40.231"
            //let host = "98.51.182.241"
            let port: UInt16 = 1883
            let clientID = self.clientID()
            
            mqttSession = MQTTSession(host: host, port: port, clientID: clientID, cleanSession: true, keepAlive: 15, useSSL: false)
            mqttSession.delegate = self
        print("Trying to connect to \(host) on port \(port) for clientID \(clientID)")

            mqttSession.connect { (error) in
                if error == .none {
                    print("Connected.")
                    self.subscribeToChannel()
                } else {
                    print("Error occurred during connection:")
                    print(error.description)
                }
            }
        }
    func publish(msg: String, channel: String) {
        let data = msg.data(using: .utf8)!
    mqttSession.publish(data, in: channel, delivering: .atMostOnce, retain: false) { (error) in
           switch error {
           case .none:
               print("Published \(msg) on channel \(channel)")
           default:
               print("Error Occurred During Publish:")
               print(error.description)
           }
       }
    }
    func clientID() -> String {

            let userDefaults = UserDefaults.standard
            let clientIDPersistenceKey = "clientID"
            let clientID: String

            if let savedClientID = userDefaults.object(forKey: clientIDPersistenceKey) as? String {
                clientID = savedClientID
            } else {
                clientID = randomStringWithLength(5)
                userDefaults.set(clientID, forKey: clientIDPersistenceKey)
                userDefaults.synchronize()
            }
            
            return clientID
        }
        
        //http://stackoverflow.com/questions/26845307/generate-random-alphanumeric-string-in-swift
        func randomStringWithLength(_ len: Int) -> String {
            let letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

            var randomString = String()
            for _ in 0..<len {
                let length = UInt32(letters.count)
                let rand = arc4random_uniform(length)
                let index = String.Index(encodedOffset: Int(rand))
                randomString += String(letters[index])
            }
            return String(randomString)
        }
}
