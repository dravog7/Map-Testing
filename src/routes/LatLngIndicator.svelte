<script lang="ts">
	import type { LeafletMouseEvent } from 'leaflet';
	import { Popup, type Map } from 'sveaflet';

	export let mapInstance: Map;
	$: popupLatLng = null as Number[] | null;

	$: if (mapInstance) {
		mapInstance.on('click', onMapClick);
	}

	function onMapClick(e: LeafletMouseEvent) {
		popupLatLng = [e.latlng.lat, e.latlng.lng];
	}
</script>

{#if popupLatLng}
	<div
		class="absolute bottom-0 left-0 bg-white w-auto rounded-sm shadow-md"
		style="z-index: 1000;"
	>
	<span class="p-2">{popupLatLng[1]+" , " + popupLatLng[0] }</span>
</div>
{/if}
