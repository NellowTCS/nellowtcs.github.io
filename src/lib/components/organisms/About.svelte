<script>
	import SparklingHighlight from '$lib/components/molecules/SparklingHighlight.svelte';
	import Socials from '$lib/components/molecules/Socials.svelte';
	import Image from '../atoms/Image.svelte';
</script>

<section id="about">
	<div class="info">
		<h2>
			I'm a developer with some
			<SparklingHighlight color="secondary">cool projects!</SparklingHighlight>
		</h2>
		<p>
			I know JavaScript, TypeScript, HTML, CSS, C and C++ (not that good at those tho), and some Rust! <br>
		    Check out some of my projects on my GitHub or read about them at the blog.
		</p>
		<div class="socials">
			<span>Socials:</span>
			<Socials />
		</div>
	</div>
	<div class="image">
		<figure>
			<Image src="/images/frontpage.png" alt="Sample for the static template" />
			<figcaption>HTMLPlayer v2</figcaption>
		</figure>
	</div>
</section>

<style lang="scss">
	@import '$lib/scss/breakpoints.scss';

	#about {
		position: relative;
		display: grid;
		grid-template-columns: 500px 500px;
		align-items: center;
		justify-content: space-between;
		padding-bottom: 50px;

		@include for-phone-only {
			grid-template-columns: 1fr;
			justify-items: center;
			gap: 20px;
		}

		.info {
			grid-column: 1; // move text to right column
			display: flex;
			flex-direction: column;
			gap: 10px;

			h2 {
				@include for-phone-only {
					text-align: center;
				}
			}

			p {
				@include for-phone-only {
					text-align: justify;
				}
			}

			@include for-phone-only {
				gap: 20px;
			}
		}

		.socials {
			display: flex;
			align-items: center;
			gap: 15px;

			@include for-phone-only {
				justify-content: center;
				margin-bottom: 10px;
				span {
					display: none;
				}
			}
		}

		.image {
			grid-column: 2; // put image in left column
			width: 500px;
			height: 300px;
			margin-left: 0;
			margin-right: auto;

			@include for-phone-only {
				grid-column: auto;
			}

			figure {
				margin: 0;
				text-align: center;
			}

			figcaption {
				margin-top: 8px;
				font-size: 0.9rem;
				color: #666;
			}
		}
	}
</style>
