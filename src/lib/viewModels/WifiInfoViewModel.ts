/* eslint-disable @typescript-eslint/no-unused-vars */
import { derived, readable } from "svelte/store";
import jsonData from "../data/signals.json";

export const wifiInfo = readable([],(set) => {
	const interval = setInterval(async () => {
		set(await getData());
	}, 5000);

    return function stop() {
		clearInterval(interval);
	};
})

async function getData() {
    const response = await fetch("https://2a61-111-92-71-122.ngrok-free.app/signals",{
        headers: {
            "Accept" : "application/json",
            "Cookie":"abuse_interstitial=2a61-111-92-71-122.ngrok-free.app"
        }
    });
    console.log("collected data!");
    console.log(await response.text())
    return await response.json()
}