/* eslint-disable @typescript-eslint/no-unused-vars */
import { derived, readable } from "svelte/store";
import jsonData from "../data/pred_signals.json";

export const wifiInfo = readable([],(set) => {
	const interval = setTimeout(async () => {
		set(await getData());
	}, 10000);

    return function stop() {
		// clearInterval(interval);
	};
})

async function getData() {
    return jsonData
    // const response = await fetch("https://proximityserverapi20240813112240.azurewebsites.net/signals",{
    //     headers: {
    //         "Accept" : "application/json",
    //     }
    // });
    // console.log("collected data!");
    // // console.log(await response.text())
    // return await response.json()
}