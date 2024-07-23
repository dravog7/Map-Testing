<script lang="ts">
	import { ImageOverlay, Map, TileLayer } from 'sveaflet';
	import overlayImage from '$lib/images/map.png';
	import mapInfo from '$lib/utils/mapOptions';
	import { wifiInfo } from '$lib/viewModels/WifiInfoViewModel';
	import ClickableMarker from './ClickableMarker.svelte';
	import LatLngIndicator from './LatLngIndicator.svelte';
	import WifiInfoDisplay from './WifiInfoDisplay.svelte';

	let map: Map;
	let clicked: number | null = null;
</script>

<div class="w-full h-screen">
	<Map
		options={{
			center: [10.011411, 76.366505],
			zoom: 24
		}}
		bind:instance={map}
	>
		<TileLayer url={mapInfo.mapUrl} options={mapInfo.option} />
		<!-- <ImageOverlay 
			url={overlayImage} 
			bounds={[
			[10.011649,76.366796],
			[10.011176,76.36672]
			]}
			/> -->
		<LatLngIndicator mapInstance={map} />
		{#each $wifiInfo as device, i}
			<ClickableMarker
				position={[device.location.latitude, device.location.longitude]}
				on:click={(e) => {
					clicked = i;
				}}
			/>
		{/each}
	</Map>
</div>
{#if clicked != null}
	<div class="absolute inset-y-10 right-0 bg-white w-auto overflow-y-scroll rounded-md shadow-md" style="z-index: 1000;">
		<WifiInfoDisplay wifiInfo={$wifiInfo[clicked]} index={clicked} />
	</div>
{/if}
