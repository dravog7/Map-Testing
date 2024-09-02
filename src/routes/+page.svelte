<script lang="ts">
	import { CircleMarker, ImageOverlay, Map, TileLayer } from 'sveaflet';
	import mapInfo from '$lib/utils/mapOptions';
	import planInfo from '$lib/utils/planOptions';
	import { wifiInfo } from '$lib/viewModels/WifiInfoViewModel';
	import ClickableMarker from './ClickableMarker.svelte';
	import LatLngIndicator from './LatLngIndicator.svelte';
	import WifiInfoDisplay from './WifiInfoDisplay.svelte';
	import { MarkerCluster } from 'sveaflet-markercluster';
	import wifiIcon from '$lib/images/wifi.svg';
	import deviceIcon from '$lib/images/device.svg';
	import predictionIcon from '$lib/images/prediction.svg';
	import piIcon from '$lib/images/pi.svg';
	import L from 'leaflet';

	let map: Map;
	let clicked: number | null = null;
	let deviceId: string = '';

	function getIcon(device: any,selected: string){
		if(selected && device.deviceId.includes(selected))
			return wifiIcon;//'red';
		// else if(device.deviceId.startsWith("ap-"))
		// 	return wifiIcon;
		// else if(device.deviceId.startsWith("prediction"))
		// 	return predictionIcon;
		else if(device.deviceType === 2)
			return piIcon;
		else
			return deviceIcon;
	}
</script>

<div class="absolute inset-x-0 top-0 h-auto rounded-md flex justify-center" style="z-index: 1000;">
	<input class="bg-white m-4" type="text" placeholder="deviceId" bind:value={deviceId} />
	<span></span>
</div>
<div class="w-full h-screen">
	<Map
		options={{
			center: planInfo.center, //[10.011411, 76.366505],
			zoom: planInfo.zoom,
			crs: planInfo.crs,
			minZoom:planInfo.minZoom,
		}}
		bind:instance={map}
	>
		<ImageOverlay 
			url={planInfo.image} 
			bounds={planInfo.bounds}
			/>
		<LatLngIndicator mapInstance={map} />
		<!-- {#each $wifiInfo as device, i (i)}
			<ClickableMarker
				position={[device.location.latitude, device.location.longitude]}
				icon={getIcon(device,deviceId)}
				on:click={(e) => {
					clicked = i;
				}}
			/>
		{/each} -->
		<CircleMarker
		latLng={[0,0]}
		options={{radius:10, color:"#ff8f8f"}}
		/>
	</Map>
</div>
{#if clicked != null}
	<div
		class="absolute inset-y-10 right-0 bg-white w-auto overflow-y-scroll rounded-md shadow-md"
		style="z-index: 1000;"
	>
		<WifiInfoDisplay wifiInfo={$wifiInfo[clicked]} index={clicked} />
	</div>
{/if}
