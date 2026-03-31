<script lang="ts">
	import ContentSection from '$lib/components/organisms/ContentSection.svelte';
	import ProjectCard from '$lib/components/molecules/ProjectCard.svelte';
	import type { Project } from '$lib/utils/types';

	export let data: {
		projects: Project[];
	};

	let { projects } = data;
</script>

<div class="container">
	<ContentSection title="All Projects" description="Check out what I've been working on.">
		<div class="grid">
			{#each projects as project}
				<ProjectCard
					title={project.title}
					coverImage={project.coverImage}
					excerpt={project.excerpt}
					slug={project.slug}
					tags={project.tags}
					link={project.link}
					repo={project.repo}
				/>
			{/each}
		</div>
	</ContentSection>
</div>

<style lang="scss">
	@import '$lib/scss/_mixins.scss';

	.grid {
		width: 100%;
		display: grid;
		grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
		grid-gap: 20px;

		@include for-tablet-portrait-down {
			grid-template-columns: 1fr;
		}

		@include for-tablet-landscape-up {
			> :global(:nth-child(6n + 1)) {
				grid-column: span 6;
			}
			> :global(:nth-child(6n + 2)) {
				grid-column: span 3;
			}
			> :global(:nth-child(6n + 3)) {
				grid-column: span 3;
			}
			> :global(:nth-child(6n + 4)),
			:global(:nth-child(6n + 5)),
			:global(:nth-child(6n + 6)) {
				grid-column: span 2;
			}
		}
	}
</style>
