FROM debian:latest

ENV DEBIAN_FRONTEND noninteractive

# Install all TeX and LaTeX dependences
# keep all installs although probably present in base image to make them explicit
RUN apt-get update && \
  apt-get install --yes --no-install-recommends \
  # basics
  make \
  ca-certificates \
  # latex
  lmodern \
  texlive-latex-base \
  texlive-generic-extra \
  texlive-fonts-extra \
  texlive-fonts-recommended \
  texlive-generic-recommended \
  texlive-lang-english \
  latex-xcolor \
  texlive-math-extra \
  texlive-latex-extra \
  texlive-bibtex-extra \
  texlive-full \
  fonts-freefont-ttf \
  fonts-freefont-otf \
  fonts-roboto \
  fonts-roboto-fontface \
  biber \
  fontconfig \
  texlive-xetex \
  cabextract \
  xfonts-utils \
  libimage-exiftool-perl
RUN apt-get install --yes python3
RUN apt-get autoclean && apt-get --purge --yes autoremove && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Export the output data
COPY . /home/root/project
WORKDIR /home/root/project

VOLUME ["/home/root/project"]

CMD ["/bin/bash"]
