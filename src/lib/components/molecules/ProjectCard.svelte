<script lang="ts">
	import Card from '#lib/components/atoms/Card.svelte';
	import Tag from '#lib/components/atoms/Tag.svelte';
	import Image from '../atoms/Image.svelte';

	export let title: string;
	export let coverImage: string | undefined = undefined;
	export let excerpt: string;
	export let slug: string;
	export let tags: string[] | undefined;
	export let link: string | undefined = undefined;
	export let repo: string | undefined = undefined;
	export let docs: string | undefined = undefined;
	export let npm: string | undefined = undefined;
	export let cargo: string | undefined = undefined;
</script>

<Card additionalClass="project-card {!coverImage ? 'no-image' : ''}">
	<div class="image" slot="image">
		{#if coverImage}
			<Image src={coverImage} alt="Cover image of this project" />
		{/if}
	</div>
	<div class="content" slot="content">
		<p class="title">
			<a href="/projects/{slug}" class="title-link" data-sveltekit-preload-data="hover">{title}</a>
		</p>
		{#if excerpt}
			<p class="text">{excerpt}</p>
		{/if}
	</div>
	<div class="footer" slot="footer">
		{#if tags?.length}
			<div class="tags">
				{#each tags.slice(0, 3) as tag (tag)}
					<Tag>{tag}</Tag>
				{/each}
			</div>
		{/if}
		<div class="links">
			{#if link}
				<a href={link} target="_blank" rel="noopener noreferrer" class="link">Live Demo</a>
			{/if}
			{#if repo}
				<a href={repo} target="_blank" rel="noopener noreferrer" class="link secondary">GitHub</a>
			{/if}
			{#if npm}
				<a
					href="https://www.npmjs.com/package/{npm}"
					target="_blank"
					rel="noopener noreferrer"
					class="link tertiary">npm</a
				>
			{/if}
			{#if cargo}
				<a
					href="https://crates.io/crates/{cargo}"
					target="_blank"
					rel="noopener noreferrer"
					class="link tertiary">crates.io</a
				>
			{/if}
			{#if docs}
				<a href={docs} target="_blank" rel="noopener noreferrer" class="link">Docs</a>
			{/if}
		</div>
	</div>
</Card>

<style lang="scss">
	.content {
		display: flex;
		flex-direction: column;
		gap: 0px;
		align-items: flex-start;
	}

	.title {
		display: flex;
		align-items: center;
		justify-content: space-between;
		width: 100%;
		font-size: 1.2rem;
		font-family: var(--font--title);
		font-weight: 700;
	}

	.title-link {
		color: inherit;
		text-decoration: none;

		&::after {
			content: '';
			position: absolute;
			inset: 0;
			z-index: 1;
			cursor: pointer;
		}
	}

	.text {
		margin-top: 5px;
		font-size: 0.9rem;
		text-align: justify;
	}

	.tags {
		display: flex;
		align-items: center;
		gap: 5px;
		flex-wrap: wrap;
	}

	.footer {
		position: relative;
		z-index: 2;
		margin-top: 20px;
		display: flex;
		flex-direction: column;
		gap: 10px;
	}

	.links {
		display: flex;
		flex-wrap: wrap;
		gap: 8px;
	}

	.link {
		display: inline-flex;
		align-items: center;
		min-height: 44px;
		padding: 10px 14px;
		border-radius: 20px;
		font-size: 0.8rem;
		font-weight: 700;
		text-decoration: none;
		background-color: rgb(var(--color--primary-rgb));
		color: var(--color--primary-contrast);

		&:hover {
			opacity: 0.9;
		}
	}

	:global(.project-card:hover),
	:global(.project-card:focus-within) {
		box-shadow: var(--card-shadow-hover);
		transform: scale(1.01);
	}

	.link.secondary {
		background-color: rgb(var(--color--secondary-rgb));
		color: var(--color--secondary-contrast);
	}

	.link.tertiary {
		background-color: rgba(var(--color--text-rgb), 0.1);
		color: var(--color--text);
	}

	:global(.project-card .image img) {
		object-fit: cover;
	}

	:global(.project-card.no-image > .image) {
		display: none;
	}
</style>
