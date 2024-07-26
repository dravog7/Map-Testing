/* eslint-disable @typescript-eslint/no-unused-vars */
import { derived, readable } from "svelte/store";
import jsonData from "../data/pred_signals.json";

export const wifiInfo = readable(await getData(),(set) => {
	const interval = setInterval(async () => {
		set(await getData());
	}, 5000);

    return function stop() {
		clearInterval(interval);
	};
})

async function getData() {
    return jsonData
    // const response = await fetch("https://proximityserverapi20240724180956.azurewebsites.net/signals",{
    //     headers: {
    //         "Accept" : "application/json",
    //     }
    // });
    // console.log("collected data!");
    // // console.log(await response.text())
    // return await response.json()
}