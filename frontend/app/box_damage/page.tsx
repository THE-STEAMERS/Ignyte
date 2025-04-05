"use client";
import React, { useEffect, useState } from "react";
import mqtt from "mqtt";
import { AlertCircle } from "lucide-react";

const BoxDamagePage: React.FC = () => {
  const [boxDamageMessage, setBoxDamageMessage] = useState<string | null>(null);

  useEffect(() => {
    const client = mqtt.connect("mqtt.eclipseprojects.io",);

    client.on("connect", () => {
      console.log("Connected to MQTT broker");
      client.subscribe("manufacturing/anomalies");
    });

    client.on("message", (topic, message) => {
      try {
        const data = JSON.parse(message.toString());
        if (data.damage) {
          setBoxDamageMessage(data.damage);
        }
      } catch (error) {
        console.error("Error parsing MQTT message:", error);
      }
    });

    client.on("error", (err) => {
      console.error("MQTT connection error:", err);
    });

    client.on("close", () => {
      console.log("MQTT connection closed");
    });

    return () => {
      client.end();
    };
  }, []);

  return (
    <div className="flex flex-col min-h-screen bg-neutral-950 text-white p-6">
      <h1 className="text-4xl font-bold text-white mb-4 px-3 py-2">Box Damage Detection</h1>

      {boxDamageMessage && (
        <div className="bg-red-900/30 border border-red-600 p-4 rounded-lg mb-4 flex items-center gap-3">
          <AlertCircle className="w-5 h-5 text-red-500" />
          <p className="text-red-500 text-lg">{boxDamageMessage}</p>
        </div>
      )}
    </div>
  );
};

export default BoxDamagePage;