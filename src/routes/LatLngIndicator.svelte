<script lang="ts">
	import type { LeafletMouseEvent } from "leaflet";
	import { Popup, type Map } from "sveaflet";

    export let mapInstance: Map;
    $: popupLatLng = [10.011411, 76.366505];
	$: popupContent = '';

    $: if (mapInstance) {
		mapInstance.on('click', onMapClick);
	}

	function onMapClick(e: LeafletMouseEvent) {
		popupLatLng = [e.latlng.lat, e.latlng.lng];
		popupContent = 'You clicked the map at ' + e.latlng.toString();
	}
</script>

{#if popupContent != ''}
<Popup
    latLng={[popupLatLng[0], popupLatLng[1]]}
    options={{
        content: popupContent
    }}
/>
{/if}